# Serverless Services

This project is created using <b>serverless framework</b>, it has an API Key generator (you have to register with e-mail --it does not require to verify the e-mail).
After getting the API Key, you can start using the API which has some authentication verifier (It verifies if the API Key that the client is using is already created).

To use:

1.The voice recognition service, the client has to send an audio (.wav file) encoded as base64 --you have to convert the audio file as base64 before sending it to the webservice.
  -It returns back a string with the detected speech in the audio file  
2.The face detection service, the client has to send an image encoded as base64 --you have to convert the image file as base64 before sending it to the webservice.
  -It returns back an array with json objects that contains the starting coordinates and the width + height for every face detected in the image 
  
  
<i>This repo will be developed more in the future by adding other services for the clients to use.</i>

