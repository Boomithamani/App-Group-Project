var div = document.getElementByClassName("answer");
var display = 0;

function hideShow()
{
    if (display == 0)
    {
        div.style.display = "block";
        display = 1;
    }
    else
    {
        div.style.display = "none";
        display = 0;
    }
}