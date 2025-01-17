# Formula to Latex

<div align="center">
  <img src="doc/font_logo.png" alt="Formula to Latex Logo">
</div>

## Overview
논문의 수식을 Latex 형식으로 자동 변환하는 도구입니다. PDF 형식의 논문에서 수식을 자동으로 감지하고, 이를 Latex 코드로 변환하여 논문 번역과 리뷰 작성을 더욱 수월하게 만들어줍니다.

## Key Features

### 1. WebUI-based Formula Conversion
- PDF 드래그 앤 드롭으로 논문 로드
- 마우스 드래그로 수식 영역 선택
- 실시간 Latex 코드 변환 및 복사 기능

### 2. Automatic Paper Formula Conversion
- YOLO v8을 통한 자동 수식 감지
- 감지된 모든 수식의 일괄 변환
- CSV 형태로 결과 저장

## Models Used

### 1. [Pix2tex - LaTexOCR](https://github.com/lukas-blecher/LaTeX-OCR)
이미지 형태의 수식을 Latex 코드로 변환하는 OCR 모델

### 2. [YOLO v8](https://github.com/ultralytics/ultralytics)
논문 내의 수식 영역을 자동으로 감지하는 객체 탐지 모델

## Installation & Setup

### Prerequisites
```bash
torch
torchvision
PyQt5
fitz
opencv-python
ultralytics
pix2tex
```

### Install
```bash
pip install -r requirements.txt
```

### WebUI Execution
```bash
python Formula_WebUI.py
```

### CSV Conversion Execution
1. [best.pt 모델 다운로드](https://drive.google.com/file/d/1tCwXJIUm3YN_GQMrcpkWb7w-mw3s7aq5/view?usp=sharing)
2. 필요한 폴더 생성
```bash
mkdir formula_image output_image pdf_image
```
3. 실행
```bash
python Formula_csv.py --pfp "논문_경로.pdf"
```

## Usage Guide

### WebUI Instructions
1. WebUI 실행 후 흰색 영역에 PDF 드래그
2. 원하는 수식 영역을 마우스로 드래그하여 선택
3. 2-3초 대기 후 하단에 변환된 Latex 코드 확인
4. 'Copy Text' 버튼으로 코드 복사

### CSV Conversion Guide
1. 명령어 실행 후 자동 변환 대기
2. 변환 완료 시 output.csv 파일 확인
3. CSV 파일에서 필요한 Latex 코드 복사하여 사용

## Project Structure
```
├── Formula_WebUI.py     # WebUI 구현
├── Formula_csv.py       # CSV 변환 구현
├── doc/                 # 문서 및 이미지
├── formula_image/       # 추출된 수식 이미지
├── output_image/        # 결과 이미지
└── pdf_image/          # 변환된 PDF 이미지
```

## Achievements & Limitations

### Key Achievements
- 논문 리뷰 시 수식 입력 자동화
- 처음 보는 수학 기호의 Latex 코드 자동 변환
- 논문 번역 시 수식 처리 효율화

### Current Limitations
- 여러 줄의 수식 인식률 저하
- UI/UX 개선 필요
- 학습 데이터 부족

## Team Composition
- AI빅데이터융합경영학과 딥러닝 논문 분석 학회 X:AI 4기 CV2 TEAM
- 팀원: 황건하, 이승학, 유광열, 이서연

## Project Duration
2023.07.06 ~ 2023.09.18

## Team Reviews

<details>
<summary>황건하</summary>
<br>
X:AI학회에서 나의 두번째 Computer Vision 토이 프로젝트를 진행할 수 있음에 감사하였다. 지금까지는 Classification만 해봤었는데, Labeling, Detection, WebUI 등 많은 것을 경험할 수 있었고 부족한 실력을 사랑으로 품어준 우리 팀원들께 고맙다. 실력을 기른 뒤 Pose Estimation, Diffusion 등 다양한 Computer Vision 토이 프로젝트 멘토가 되어 배웠던 것을 후배들에게 나눠주길 소망한다.
</details>

<details>
<summary>이승학</summary>
<br>
프로젝트를 구상부터 구현까지 진행하면서 여러 시행착오가 있었지만 최종적인 결과물이 잘 나온 거 같아서 기분이 좋습니다. 특히 모델 학습 및 추론뿐만이 아니라 GUI 구성까지 짜보는 경험까지 해서 많은 것을 배운 프로젝트였던 것 같습니다. 비록 수식이 여러 줄 입력되었을 때 잘 인식하지 못한다는 아쉬움이 있지만, 추후 발전시켜 해결해 보고 싶습니다.
</details>

<details>
<summary>유광열</summary>
<br>
다양한 논문 리뷰를 진행하면 수식 부분에서 많은 시간이 걸렸다. 이를 해결하기 위해 pdf로 된 논문에서 손쉽게 수식을 출력하기 위해 Formula2Latex 프로젝트를 진행하게 되었다. 해당 프로젝트를 통해 YOLO, PyQT를 더 잘 다루고 여러 데이터를 다루어 볼 수 있는 좋은 기회였다. 생각했던 것보다 결과물이 더 좋게 나와 앞으로도 논문 리뷰를 진행할 때 애용할 거 같다.
</details>

<details>
<summary>이서연</summary>
<br>
'Formula to Latex'라는 주제를 WebUI를 이용한 방법과 Detection을 통해 모든 수식을 변환하는 방법 2가지로 구현할 수 있어 좋았다. 데이터 라벨링부터, Detection, WebUI 제작 등 많은 경험을 할 수 있었던 프로젝트였다. 여러 시행착오가 있었으나 원하는 결과물을 얻었을 때 큰 성취감을 느꼈으며, 한 단계 성장하는 계기가 되었다.
</details>

## References
- [중간 발표 자료](https://github.com/X-AI-eXtension-Artificial-Intelligence/4th-ADV-SESSION/blob/main/TeamCV2/doc/XAI%20%E1%84%8C%E1%85%AE%E1%86%BC%E1%84%80%E1%85%A1%E1%86%AB%20%E1%84%87%E1%85%A1%E1%86%AF%E1%84%91%E1%85%AD%20%E1%84%8C%E1%85%A1%E1%84%85%E1%85%AD.pdf)
- [최종 발표 자료](https://github.com/X-AI-eXtension-Artificial-Intelligence/4th-ADV-SESSION/blob/main/TeamCV2/doc/XAI%20%E1%84%8E%E1%85%AC%E1%84%8C%E1%85%A9%E1%86%BC%20%E1%84%87%E1%85%A1%E1%86%AF%E1%84%91%E1%85%AD%20%E1%84%8C%E1%85%A1%E1%84%85%E1%85%AD.pdf)

