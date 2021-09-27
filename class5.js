function changeText() {
    var span = document.getElementById("text");
    span.innerText = "你好，网安学院！";
}

function addItem() {
    var ulParent = document.getElementById("ul-el");

    var liChild = document.createElement("li");
    liChild.innerText = "新增标签";

    ulParent.append(liChild);
}