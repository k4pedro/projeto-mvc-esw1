import flet as ft
from views.loginView import LoginView
from views.dashboardAdminView import DashboardAdminView
from views.dashboardAgenteView import DashboardAgenteView
from views.relatorioView import RelatorioView
from views.atendimentoMeiView import AtendimentoMeiView
from views.atendimentoNaoMeiView import AtendimentoNaoMeiView
from views.consultaAtendimentoView import ConsultaAtendimentoView

class ControladorRoutes:
    def __init__(self, page):
        self.page = page

    def route_change(self, route):
        self.page.views.clear()
        
        if self.page.route == "/":
            self.page.views.append(ft.View("/", [LoginView(self.page)]))
        elif self.page.route == "/dashboard_admin":
            self.page.views.append(ft.View("/dashboard_admin", [DashboardAdminView(self.page)]))
        elif self.page.route == "/dashboard_agente":
            self.page.views.append(ft.View("/dashboard_agente", [DashboardAgenteView(self.page)]))
        elif self.page.route == "/relatorio":
            self.page.views.append(ft.View("/relatorio", [RelatorioView(self.page)]))
        elif self.page.route == "/atendimento_mei":
            self.page.views.append(ft.View("/atendimento_mei", [AtendimentoMeiView(self.page)]))
        elif self.page.route == "/atendimento_nao_mei":
            self.page.views.append(ft.View("/atendimento_nao_mei", [AtendimentoNaoMeiView(self.page)]))
        elif self.page.route == "/consulta_atendimento":
            self.page.views.append(ft.View("/consulta_atendimento", [ConsultaAtendimentoView(self.page)]))
        
        self.page.update()
