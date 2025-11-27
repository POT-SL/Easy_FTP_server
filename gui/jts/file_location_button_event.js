"use strict";
// 等待 DOM 加载完成
document.addEventListener('DOMContentLoaded', () => {
    // 绑定按钮事件
    const choice_locaion = document.getElementById('choice_locaion');
    const open_locaion = document.getElementById('open_locaion');
    // 选择文件夹
    choice_locaion.addEventListener('click', (event) => {
        console.log('Choice Folder.');
    });
    // 打开文件夹
    open_locaion.addEventListener('click', (event) => {
        console.log('Open Folder.');
    });
});
