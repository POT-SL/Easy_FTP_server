// 获取所有需要处理的 input 元素
const timeInputs = document.querySelectorAll('input[type="number"]');

// 遍历每个 input 并添加事件监听
timeInputs.forEach(input => {
    input.addEventListener('blur', function() {
        // 1. 获取原始输入值和边界
        const rawValue = this.value;
        const min = parseInt(this.min, 10);
        const max = parseInt(this.max, 10);

        // 2. 将输入值转为整数，如果无效则设为最小值
        let finalValue = parseInt(rawValue, 10);
        if (isNaN(finalValue)) {
            finalValue = min;
        }

        // 3. 进行范围限制，得到最终的、正确的数值
        if (finalValue < min) {
            finalValue = min;
        } else if (finalValue > max) {
            finalValue = max;
        }

        // 4. 格式化最终数值为两位数字符串
        // 使用 padStart 是最现代、最简洁的方法
        const displayValue = String(finalValue).padStart(2, '0');

        // 5. 更新输入框的显示
        this.value = displayValue;
    });
});