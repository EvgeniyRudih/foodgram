def format_shopping_cart(ingredients):
    lines = ['Список покупок:\n']
    for item in ingredients:
        lines.append(
            f'- {item["ingredient__name"]} '
            f'({item["ingredient__measurement_unit"]}) — '
            f'{item["amount_sum"]}'
        )
    return '\n'.join(lines)
