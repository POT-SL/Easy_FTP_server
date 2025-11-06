"use strict";
// 等待元素加载完成
document.addEventListener('DOMContentLoaded', () => {
    // 绑定按钮事件
    const taskbar_status = document.getElementById('taskbar_status');
    const taskbar_ftpset = document.getElementById('taskbar_ftpset');
    const taskbar_system = document.getElementById('taskbar_system');
    const taskbar_about = document.getElementById('taskbar_about');
    // 绑定头元素
    const main_gui = document.getElementById('gui_main');
    // 按钮事件
    taskbar_status.addEventListener('click', (event) => {
        main_gui.style.transition = 'transform 0.3s cubic-bezier(0,.85,0,1)';
        main_gui.style.transform = 'translateY(0)';
        console.log('Page 1');
    });
    taskbar_ftpset.addEventListener('click', (event) => {
        main_gui.style.transition = 'transform 0.3s cubic-bezier(0,.85,0,1)';
        main_gui.style.transform = 'translateY(-25%)';
        console.log('Page 2');
    });
    taskbar_system.addEventListener('click', (event) => {
        main_gui.style.transition = 'transform 0.3s cubic-bezier(0,.85,0,1)';
        main_gui.style.transform = 'translateY(-50%)';
        console.log('Page 3');
    });
    taskbar_about.addEventListener('click', (event) => {
        main_gui.style.transition = 'transform 0.3s cubic-bezier(0,.85,0,1)';
        main_gui.style.transform = 'translateY(-75%)';
        console.log('Page 4');
    });
});
