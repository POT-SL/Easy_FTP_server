"use strict";
// 等待 DOM 加载完成
document.addEventListener('DOMContentLoaded', () => {
    const autoStartCheckbox = document.getElementById('auto_start');
    autoStartCheckbox.addEventListener('change', (event) => {
        const isChecked = event.target.checked;
        // 你也可以在这里添加其他逻辑
        if (isChecked) {
            console.log('auto_start_button: "on"');
        }
        else {
            console.log('auto_start_button: "off"');
        }
    });
});
