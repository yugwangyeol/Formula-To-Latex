import fitz
import argparse
import os
import cv2
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from pix2tex.cli import LatexOCR
import pandas as pd
from PIL import Image, ImageDraw
from matplotlib import image as mpimg
from ultralytics import YOLO


def pdf_to_images(pdf_path):
    output_folder = "../pdf_image"
    pdf_document = fitz.open(pdf_path)
    
    for page_num in range(pdf_document.page_count):
        page = pdf_document[page_num]
        image = page.get_pixmap(matrix=fitz.Matrix(4.0,4.0))
        
        image_path = f"{output_folder}/page_{page_num + 1}.png"
        image.save(image_path)
        print(f"Page {page_num + 1} saved as {image_path}")
    
    pdf_document.close()

def formula_detection(treshhold=0.5):
    output_folder = "../pdf_image"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    files = os.listdir(output_folder)
    model = YOLO('best.pt')

    for page_idx,file in enumerate(files):
        img_fp = f'{output_folder}/{file}'
        image = cv2.imread(img_fp)

        detection = model(image)[0]
        score_threshold = treshhold

        image = Image.open(img_fp)
        draw = ImageDraw.Draw(image)

        for data in detection.boxes.data.tolist():
            confidence = float(data[4])
            if confidence < score_threshold:
                continue

            xmin, ymin, xmax, ymax = int(data[0]), int(data[1]), int(data[2]), int(data[3])

            draw.rectangle([xmin, ymin, xmax, ymax], outline="green", width=3)

        # detection_save
        save_path = f'../output_image/{page_idx}.png'
        image.save(save_path)
        print(f"이미지가 {save_path} 경로에 저장되었습니다.")

        image_path = img_fp
        image = Image.open(image_path)
        draw = ImageDraw.Draw(image)

        output_dir = '../formula_image'
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        score_threshold = treshhold

        for idx,data in enumerate(detection.boxes.data.tolist()):
            confidence = float(data[4])
            if confidence < score_threshold:
                continue

            x_min, y_min, x_max, y_max = int(data[0]), int(data[1]), int(data[2]), int(data[3])
            cropped_image = image.crop((x_min, y_min, x_max, y_max))  # 이미지 자르기
            save_path = os.path.join(output_dir, f'cropped_image_{page_idx}_{idx}.jpg')

                # 이미지 저장
            cropped_image.save(save_path)
            print(f'Cropped image saved: {save_path}')


def formula_csv():
    model = LatexOCR()
    files = os.listdir('../formula_image')

    formula_latexs = []
    formula_names = []

    for file in files:
        img = Image.open(f'../formula_image/{file}')
        formula_latex = model(img)
        formula_name = file.split('.')[0]

        if formula_latex is None:
            formula_latex = 'No formula'
        
        formula_latexs.append(formula_latex)
        formula_names.append(formula_name)
    
    output_df = pd.DataFrame({'Latex_position':formula_names,'Latex':formula_latexs})
    output_df.to_csv('../output.csv',index=False)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--pfp')

    args = parser.parse_args()

    # PDF 파일 경로와 이미지를 저장할 폴더 지정
    pdf_file_path = args.pfp

    # 이미지로 변환
    pdf_to_images(pdf_file_path)
    formula_detection(0.5)
    formula_csv()
    print('완료')

if __name__ == "__main__":
    main()


# python Formula_csv.py --pfp "../../논문/Nerf/Nerf.pdf"
