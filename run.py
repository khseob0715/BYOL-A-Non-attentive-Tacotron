## import library
from tacotron import get_vocgan
from tacotron.model import NonAttentiveTacotron
from tacotron.tokenizer import BaseTokenizer
import torch
import IPython.display as ipd
from scipy.io.wavfile import write
import os
import locale
import sys





from by.byol_a.common import seed_everything, load_yaml_config





# 시스템 로케일을 가져와 인코딩 설정하기
sys.stdin = open(sys.stdin.fileno(), mode='r', encoding=locale.getpreferredencoding())

def run(InputText, lang):
    ## set device
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    # if torch.cuda.is_available() else 'cpu'

    tacotron_path = './model'

    if lang == 1:
        # 한글
        tacotron_path = './model/korean'
    else:
        # 영문 
        tacotron_path = './model'  

    ## set pretrained model path
    generator_path = './generator/ljspeech_29de09d_4000.pt'

    if lang == 1:
        # 한글
        generator_path = './generator/kss_29de09d_4500.pt'
    else:
        # 영문
        generator_path = './generator/ljspeech_29de09d_4000.pt'

    ## load tacotron model
    tacotron = NonAttentiveTacotron.from_pretrained(tacotron_path)
    tacotron.to(device)
    tacotron.eval()

    ## load tokenizer
    tokenizer = BaseTokenizer.from_pretrained(tacotron_path)

    ## Inference
    text = InputText

    encoded_text = tokenizer.encode(text)
    encoded_torch_text = {key: torch.tensor(item, dtype=torch.long)
                          .unsqueeze(0).to(device) for key, item in encoded_text.items()}

    print(encoded_text)

    


    ## load generator model
    generator = get_vocgan(generator_path)
    generator.to(device)
    generator.eval()



    with torch.no_grad():
        ## make log mel-spectrogram
        tacotron_output = tacotron.inference(**encoded_torch_text)
        
        ## make audio
        audioData = generator.generate_audio(**tacotron_output)

        # ipd.Audio(audio, rate=tacotron.sampling_rate)

        # display(audioData)

        filename = 'my_audio.wav'

        write(filename, tacotron.sampling_rate, audioData)

        # 윈도우 하위 프로그램 리눅스에서만 실행 가능 .
        os.system("explorer.exe " + filename)

if __name__ == '__main__':
    lang = int(input('영어면 0 을 한글이면 1을 입력해주세요: '))

    text = input('생성할 입력 문자를 작성해주세요 : ')
    
    results = run(text, lang)