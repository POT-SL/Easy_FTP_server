"use strict";
// 获取按钮和div元素
const editUserButton = document.getElementById('edit_user');
const pswChangeDiv = document.getElementById('psw_change');
// 检查元素是否存在
if (editUserButton && pswChangeDiv) {
    // 为按钮添加点击事件监听器
    editUserButton.addEventListener('click', () => {
        // 显示div元素
        pswChangeDiv.style.display = 'flex'; // 或者使用 'flex', 'inline-block' 等，根据你的布局需要
    });
}
