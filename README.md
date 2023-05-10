# BYOL-A-Non-attentive-Tacotron
Speech Information Processing project

## Paper 
Self-supervised learning for robust voice cloning

* Pre-train: BYOL-A
* Arcitecture: Non-Attentive Tacotron
* vocoder: LPC Net


* Dataset: VCTK Dataset



https://drive.google.com/file/d/1XV7WLYdvp2uecxhTfgPM_9nVaDJmBiPv/view?usp=share_link

구글 드라이브에 pre-trained model 이랑 데이터셋 일부를 zip으로 만들어놔서 올려놓았습니다. 

다운 받아서 압축을 푼 다음에, 복사해간 프로젝트에 넣어놔야 정상적으로 동작합니다. 



그런 다음에, run.py 를 실행시키면 Non-Attentive Tacotron project가 실행됩니다. 

0 누르면, 영어로... 1 누르면, 한글로... 생성이 가능하고요. 

생성된 wav 파일은 바로 재생되도록 구현해놓았습니다. 




### Reference
Original Code: Not Available

Non-Attentive Tacotron Code:   https://github.com/JoungheeKim/Non-Attentive-Tacotron

BYOL-A Code: https://github.com/nttcslab/byol-a

