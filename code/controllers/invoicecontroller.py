from entitys.invoice import Invoice
from view.invoiceview import InvoiceView

class InvoiceController:

    def__init__(self):
        self.__invoiceview = InvoiceView(self)
        self.__invoice = []
    
    def inicia(self)
        self.abre_tela_inicia()

    def inclui_invoice(self):
        Invoice = self.busca_pagamento_pelo_id(id_payment)
        if not Invoice:
            self.__invoice.append(Invoice)
    
    def atualizar_invoice(self):

    def exclui_part(self):
        if part in self.__part:
            self.__part.remove(part)

    def lista_part(self):
        return self.__invoice

    def generate_report(self):
        report = []
        report.append("Invoice Report\n")
        report.append(f"Total Invoices: {len(self.__invoice)}\n")
        report.append("Invoice List:\n")
        for invoice in self.__invoice:
            report.append(f"{invoice}\n")
        return "".join(report)

    def finalizar(self):
        exit(0)

    def abre_tela_inicial (self):
        switcher = {0: self.finalizar, 1:self.inclui_part, 2:self.alterar_part, 3:self.exclui_part, 4:self.lista_client, 5:self.generate_report}

        while True:
            opcao = self.__view_client.mostra_tela_opcoes()
            funcao_escolhida = switcher[opcao]
            funcao_escolhida ()


    
   