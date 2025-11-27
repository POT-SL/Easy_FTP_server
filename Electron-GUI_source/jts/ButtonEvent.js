"use strict";
//绑定按钮
const taskbar_status = document.getElementById('taskbar_status');
const taskbar_ftpset = document.getElementById('taskbar_ftpset');
const taskbar_system = document.getElementById('taskbar_system');
const taskbar_about = document.getElementById('taskbar_about');
// 按钮事件
taskbar_status.addEventListener('click', (event) => {
    const data = { id: 'taskbar_status', data: {} };
    const response = fetch('/send', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data),
    });
});
taskbar_ftpset.addEventListener('click', (event) => {
    const data = { id: 'taskbar_ftpset', data: {} };
    const response = fetch('/send', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data),
    });
});
taskbar_system.addEventListener('click', (event) => {
    const data = { id: 'taskbar_system', data: {} };
    const response = fetch('/send', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data),
    });
});
taskbar_about.addEventListener('click', (event) => {
    const data = { id: 'taskbar_about', data: {} };
    const response = fetch('/send', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data),
    });
});
