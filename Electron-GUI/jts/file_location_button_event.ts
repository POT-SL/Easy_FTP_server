// 等待 DOM 加载完成
document.addEventListener('DOMContentLoaded', () => {

    // 绑定按钮事件
    const choice_locaion = document.getElementById('choice_locaion') as HTMLButtonElement
    const open_locaion = document.getElementById('open_locaion') as HTMLButtonElement

    // 选择文件夹
    choice_locaion.addEventListener('click', (event: MouseEvent) => {
        console.log('Choice Folder.')
    });

    // 打开文件夹
    open_locaion.addEventListener('click', (event: MouseEvent) => {
        console.log('Open Folder.')
    });

});
