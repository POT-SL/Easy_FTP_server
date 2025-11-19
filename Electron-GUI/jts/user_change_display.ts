document.addEventListener('DOMContentLoaded', () => {
  console.log('用户更改显示脚本已加载');
  // 获取按钮和div元素
  const editUserButton = document.getElementById('edit_user_display') as HTMLButtonElement;
  const pswChangeDiv = document.getElementById('psw_change') as HTMLDivElement;
  const pswCanelButton = document.getElementById('psw_cancel') as HTMLButtonElement;

  // 为按钮添加点击事件监听器
  editUserButton.addEventListener('click', () => {
    // 显示div元素
    console.log('编辑用户按钮被点击');
    pswChangeDiv.style.display = 'flex';
  });

  // 为取消按钮添加点击事件监听器
    pswCanelButton.addEventListener('click', () => {
      // 隐藏div元素
      console.log('取消按钮被点击');
      pswChangeDiv.style.display = 'none';
    });
});