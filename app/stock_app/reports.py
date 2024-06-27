import io
from reportlab.pdfgen import canvas
from django.http import HttpResponse
import pandas as pd

def generate_pdf_report(queryset):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="sales_report.pdf"'

    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    p.drawString(100, 800, "Relatório de Vendas")

    y = 750
    for sale in queryset:
        sale_data = f"Venda ID: {sale.id}, Produto: {sale.produto.nome}, Quantidade: {sale.quantidade}, Vendedor: {sale.vendedor.nome}"
        p.drawString(50, y, sale_data)
        y -= 30

    p.showPage()
    p.save()
    buffer.seek(0)
    response.write(buffer.getvalue())
    return response


def generate_excel_report(queryset):
    output = io.BytesIO()

    data = [{
        "Venda ID": sale.id,
        "Produto": sale.produto.nome,
        "Quantidade": sale.quantidade,
        "Vendedor": sale.vendedor.nome
    } for sale in queryset]

    df = pd.DataFrame(data)

    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Sales Report')

    output.seek(0)

    response = HttpResponse(output.getvalue(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="sales_report.xlsx"'

    return response