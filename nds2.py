payment = input('Введите сумму : ')
def get_vat(payment):
    try:
      payment = float(payment)
      vat = payment / 100 * 20
      vat = round (vat, 2)
      return ('НДС составил: {}'.format(vat))
    except (TypeError, ValueError):
      return ('Введенные данные невозможно обработать')

result = get_vat(payment)
print(result)
