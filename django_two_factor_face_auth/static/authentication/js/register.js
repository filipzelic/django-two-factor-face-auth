const constraints = {
  video: true
};

const captureVideoButton =
  document.querySelector('#video-button');
const registerButton = document.querySelector('#register-button');
const video = document.querySelector('#screenshot-video');
const image_hidden = document.querySelector('#id_image');

captureVideoButton.onclick = function() {
    captureVideoButton.setAttribute('style','display: none;');
    registerButton.removeAttribute("style");
    navigator.mediaDevices.getUserMedia(constraints).
    then(handleSuccess).catch(handleError);
};

registerButton.onclick = video.onclick = function() {
    var canvas = document.createElement("canvas");
    canvas.getContext('2d').drawImage(video, 0, 0, canvas.width, canvas.height);
    image_hidden.value = canvas.toDataURL();
    document.forms["face-register-form"].submit();
};

function handleSuccess(stream) {
  registerButton.disabled = false;
  video.srcObject = stream;
}