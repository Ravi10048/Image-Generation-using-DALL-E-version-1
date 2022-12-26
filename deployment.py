''' DALL E  is image generation model developed by openAI'''
import streamlit as st
import openai
import urllib.request # url
from PIL import Image # pillow for image processing
import cv2
import requests
import shutil
openai.api_key="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"
def image_gen(description):
    try:
        img_response = openai.Image.create(     # image will create and store
            prompt = description,      # description of image
            n=1,             # generate n images
            size="512x512")    # 256x256, 512x512, 1024x1024      support these sizes

        print(img_response)

        img_url = img_response['data'][0]['url']
        urllib.request.urlretrieve(img_url, 'image.png')
        img1 = Image.open("image.png")
        # img=cv2.imread("image.png")
        # cv2.imshow('Window',img)
        # cv2.waitKey(0)
        return img1
        # with st.expander("Grayscale Matrix details: click to read more"):
        # st.write(img)


    # saving theimage
        # cv2.imwrite('dog_grayscale_image.jpg', img)


    except:
        return "error"



l1=[]
st.title("IMAGE GENERATION USING DALL-E ")
ds=st.text_input("Write image description:-")
if st.button("Generate Image"):
  img=image_gen(ds) 
  st.success("Displaying")
  if img!="error":
    st.image(img)
  else:
    print("error")            