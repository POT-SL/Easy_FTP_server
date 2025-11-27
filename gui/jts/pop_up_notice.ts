document.addEventListener('DOMContentLoaded', () => {
    // 假设你有按钮元素
    const showPopupButton = document.getElementById('choice_locaion') as HTMLButtonElement;
    const popup = document.getElementById('pop_up') as HTMLDivElement;

    showPopupButton.addEventListener('click', () => {
        // 显示弹窗
        console.log('显示弹窗');
        popup.classList.remove('hide');
        popup.classList.add('show');
        
        // 3秒后隐藏弹窗
        setTimeout(() => {
        popup.classList.remove('show');
        popup.classList.add('hide');
        }, 1500);
    });
});