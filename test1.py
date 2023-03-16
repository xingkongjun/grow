def calculate_margin(conversion_price, margin_ratio, trade_size):
    """
    计算外汇保证金
    :param conversion_price: 转换价格
    :param margin_ratio: 保证金比率
    :param trade_size: 交易规模
    :return: 保证金
    """
    margin = conversion_price * margin_ratio * trade_size
    return margin

# 示例用法
conversion_price = 1.0611  # 转换价格
margin_ratio = 1/25  # 保证金比率
trade_size = 100000  # 交易规模

margin = calculate_margin(conversion_price, margin_ratio, trade_size)

print("所需保证金：", margin)
