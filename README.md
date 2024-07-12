![font_logo](doc/font_logo.png)

# 주제: Formula to Latex

<img width="777" alt="image" src="https://github.com/X-AI-eXtension-Artificial-Intelligence/4th-ADV-SESSION/assets/100743813/6b9801e8-26a6-4c37-a7a0-091be7549da3">

---

#### 사용 모델
* [Pix2tex - LatexOCR](https://github.com/lukas-blecher/LaTeX-OCR)
  
<img width="739" alt="image" src="https://github.com/X-AI-eXtension-Artificial-Intelligence/4th-ADV-SESSION/assets/100743813/9fc02872-52be-4603-b2ef-20c01638ffd3">


<br>
<br>
<br>
<br>

- [YOLO v8](https://github.com/HumanSignal/labelImg)

  
<img width="675" alt="image" src="https://github.com/X-AI-eXtension-Artificial-Intelligence/4th-ADV-SESSION/assets/100743813/7ebe9c83-3b50-4b7a-ade5-b668caea90bb">

<br>
<br>

* 사용시 해당 GitHub Clone 해서 사용해야 합니다.

---

#### 데이터
* [M2LATEX-100K (Kaggle)](https://www.kaggle.com/datasets/shahrukhkhan/im2latex100k)
  
<img width="328" alt="image" src="https://github.com/X-AI-eXtension-Artificial-Intelligence/4th-ADV-SESSION/assets/100743813/56e1f406-2666-4b60-a017-4decd0627eb4">

---

## 목차

- [1. 배경 및 목적](#배경-및-목적)
- [2. 주최/주관 & 팀원](#주최/주관-&-팀원)
- [3. 프로젝트 기간](#프로젝트-기간)
- [4. 프로젝트 소개](#프로젝트-소개)
- [5. WebUI Inference](#WebUI-Inference)
- [6. Formula CSV Inference](#Formula-CSV-Inference)
- [7. 느낀점](#느낀점)
- [8. 발표자료](#발표자료)

---

## 1. 배경 및 목적

* 논문 번역 시 수식 변환의 어려움 존재
* 기존에 존재하는 PDF to LaTex가 제대로 작동되지 않음
* WebUI를 통해 원하는 Formula를 변환해서 논문 번역 시 수월하게 사용할 수 있게끔 배포하는 것이 목적

---

## 2. 주최/주관 & 팀원

* 주최/주관: AI빅데이터융합경영학과 딥러닝 논문 분석 학회 X:AI 4기 CV2 TEAM
* 팀원: 총 4명 (황건하, 이승학, 유광열, 이서연)

---

## 3. 프로젝트 기간

*  2023.07.06 ~ 2023.09.18

---

## 4. 프로젝트 소개

* 논문 리뷰 또는 논문 번역 시 수식 변환을 쉽게 만들어주는 프로젝트

<img width="873" alt="image" src="https://github.com/X-AI-eXtension-Artificial-Intelligence/4th-ADV-SESSION/assets/100743813/3dc67f68-baab-4ad9-82d9-43f1b463965a">


### 4.1. 과정

* WebUI를 통해 원하는 논문의 Formula를 변환
    * YOLO v8을 통해 Formula Detection 진행
    * Pix2tex-LaexOCR model 활용
* 논문 속 모든 Formula를 Latex로 변환 후 csv로 반환
    * 반환된 Latex 언어 복사하여 사용

### 4.2. 기대효과

* 논문 리뷰 작성할 때 수식 입력이 편해짐
* 처음보는 수학 기호에 대한 Latex를 찾아 볼 필요가 없음
* 전체 논문 번역 시 자연스러운 번역 결과가 나올 것으로 기대

### 4.3.한계점

* 대량의 데이터를 활용하지 못함
* WebUI를 예쁘게 만들지 못함

---

## 5. WebUI Inference
![play](https://github.com/X-AI-eXtension-Artificial-Intelligence/4th-ADV-SESSION/assets/97331900/a5b42e61-616e-4c29-81ce-01db58071d38)
<br>
<br>
<br>

(1) python Formula_WebUI.py로 실행
<br>
<br>
(2) WebUI 흰색 영역에 PDF 형식의 논문 드래그
<br>
<br>
(3) 해당 이미지 위에서 원하는 Formula 영역을 q로 통해 지정하고 드래그
<br>
<br>
(4) 2-3초 기다리면 밑에 copy text가 나오고, 변환된 Latex 언어를 복사하여 사용

---

## 6. Formula CSV Inference

(1) <a href="https://drive.google.com/file/d/1tCwXJIUm3YN_GQMrcpkWb7w-mw3s7aq5/view?usp=sharing">best.pt 다운로드</a>
<br>
<br>
(2) formula_image, output_image, pdf_image 폴더 만들어 주기
<br>
<br>
(3) python Formula_csv.py --pfp "paper_pdf_path"
<br>
<br>
(4) output.csv 사용

---

## 7. 느낀점

**황건하**
- X:AI학회에서 나의 두번째 Computer Vision 토이 프로젝트를 진행할 수 있음에 감사하였다. 지금까지는 Classification만 해봤었는데, Labeling, Detection, WebUI 등 많은 것을 경험할 수 있었고 부족한 실력을 사랑으로 품어준 우리 팀원들께 고맙다. 실력을 기른 뒤 Pose Estimation, Diffusion 등 다양한 Computer Vision 토이 프로젝트 멘토가 되어 배웠던 것을 후배들에게 나눠주길 소망한다.

**이승학**
- 프로젝트를 구상부터 구현까지 진행하면서 여러 시행착오가 있었지만 최종적인 결과물이 잘 나온 거 같아서 기분이 좋습니다. 특히 모델 학습 및 추론뿐만이 아니라 GUI 구성까지 짜보는 경험까지 해서 많은 것을 배운 프로젝트였던 것 같습니다. 비록 수식이 여러 줄 입력되었을 때 잘 인식하지 못한다는 아쉬움이 있지만, 추후 발전시켜 해결해 보고 싶습니다.

**유광열**
- 다양한 논문 리뷰를 진행하면 수식 부분에서 많은 시간이 걸렸다. 이를 해결하기 위해 pdf로 된 논문에서 손쉽게 수식을 출력하기 위해 Formula2Latex 프로젝트를 진행하게 되었다. 해당 프로젝트를 통해 YOLO, PyQT를 더 잘 다루고 여러 데이터를 다루어 볼 수 있는 좋은 기회였다. 생각했던 것보다 결과물이 더 좋게 나와 앞으로도 논문 리뷰를 진행할 때 애용할 거 같다.

**이서연**
- 'Formula to Latex'라는 주제를 WebUI를 이용한 방법과 Detection을 통해  모든 수식을 변환하는 방법 2가지로 구현할 수 있어 좋았다. 데이터 라벨링부터, Detection, WebUI 제작 등 많은 경험을 할 수 있었던 프로젝트였다. 여러 시행착오가 있었으나 원하는 결과물을 얻었을 때 큰 성취감을 느꼈으며, 한 단계 성장하는 계기가 되었다.
---

## 8. 발표자료

* <a href="https://github.com/X-AI-eXtension-Artificial-Intelligence/4th-ADV-SESSION/blob/main/TeamCV2/doc/XAI%20%E1%84%8C%E1%85%AE%E1%86%BC%E1%84%80%E1%85%A1%E1%86%AB%20%E1%84%87%E1%85%A1%E1%86%AF%E1%84%91%E1%85%AD%20%E1%84%8C%E1%85%A1%E1%84%85%E1%85%AD.pdf">XAI 중간 발표 자료.pdf</a>

* <a href="https://github.com/X-AI-eXtension-Artificial-Intelligence/4th-ADV-SESSION/blob/main/TeamCV2/doc/XAI%20%E1%84%8E%E1%85%AC%E1%84%8C%E1%85%A9%E1%86%BC%20%E1%84%87%E1%85%A1%E1%86%AF%E1%84%91%E1%85%AD%20%E1%84%8C%E1%85%A1%E1%84%85%E1%85%AD.pdf">XAI 최종 발표 자료.pdf</a>







