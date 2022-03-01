const checkBoxes = document.getElementsByClassName("checkbox");

for (const box of checkBoxes) {
    box.addEventListener("change", checkTask);
}


function checkTask() {
    const tasks = document.getElementsByClassName("task");
    let boxTask;
    for (let task of tasks) {
        if (this.dataset.row === task.dataset.row) {
            boxTask = task;
        }
    }
    if (this.checked) {
        boxTask.innerHTML = `<s> ${boxTask.innerHTML} </s>`;
    }
    else {
        boxTask.innerHTML = boxTask.children[0].innerHTML;
    }
}