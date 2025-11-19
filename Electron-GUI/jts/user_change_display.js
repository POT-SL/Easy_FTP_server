"use strict";
document.addEventListener('DOMContentLoaded', () => {
    console.log('用户更改显示脚本已加载');
    // 获取按钮和div元素
    const editUserButton = document.getElementById('edit_user_display');
    const pswChangeDiv = document.getElementById('psw_change');
    const pswCanelButton = document.getElementById('psw_cancel');
    // 绑定通知
    const popup = document.getElementById('pop_up');
    // 为按钮添加点击事件监听器
    editUserButton.addEventListener('click', () => {
        // 显示div元素
        console.log('编辑界面');
        pswChangeDiv.style.display = 'flex';
    });
    // 为取消按钮添加点击事件监听器
    pswCanelButton.addEventListener('click', () => {
        console.log('取消');
        // 隐藏界面
        pswChangeDiv.style.display = 'none';
        //通知
        popup.style.backgroundColor = 'rgb(238, 0, 0)';
        popup.innerHTML = '<p>更改已取消</p>';
        popup.classList.remove('hide');
        popup.classList.add('show');
        setTimeout(() => {
            popup.classList.remove('show');
            popup.classList.add('hide');
        }, 1500);
    });
});
