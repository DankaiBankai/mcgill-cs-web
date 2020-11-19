// Function to change color of background of article when hovered
function changeCaptionBackground(color) {
    let captions = document.getElementsByClassName("caption");
    for(let i = 0; i < captions.length; i++){
        captions[i].style.backgroundColor = color;
    }
}