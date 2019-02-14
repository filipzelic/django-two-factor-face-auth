const constraints = {
  video: true
};

const captureVideoButton =
  document.querySelector('#video-button');
const loginButton = document.querySelector('#login-button');
const video = document.querySelector('#screenshot-video');
const image_hidden = document.querySelector('#id_image');

captureVideoButton.onclick = function() {
    captureVideoButton.setAttribute('style','display: none;');
    loginButton.removeAttribute("style");
    navigator.mediaDevices.getUserMedia(constraints).
    then(handleSuccess).catch(handleError);
};

loginButton.onclick = video.onclick = function() {
    var canvas = document.createElement("canvas");
    canvas.getContext('2d').drawImage(video, 0, 0, canvas.width, canvas.height);
    image_hidden.value = canvas.toDataURL();
    document.forms["face-login-form"].submit();
};

function handleSuccess(stream) {
  loginButton.disabled = false;
  video.srcObject = stream;
}