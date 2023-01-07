"""
Modulo responsavel pelas notificações no app
"""

import customtkinter

# contem a referencia para o label que ira mostrar a notificação
__notification_display:customtkinter.CTkLabel = None


def set_notification_display(notification_display:customtkinter.CTkLabel) -> customtkinter.CTkLabel:
  """
  Configura o display aonde as notificações serão mostradas

  :param nofication_display: referencia ao label aonde se pretende
  mostrar as notificações
  """
  global __notification_display

  __notification_display = notification_display

  return notification_display


def notification(notification_text:str) -> str:
  """
  Mostra a notificação no __notfication_display

  :param notification_text: a notificação que será mostrada na tela
  :return: o mesmo texto mostrado

  É recomendavel que a notificação não seja muito longa.
  Curta e objetiva de preferencia.
  """

  global __notification_display

  __notification_display.configure(text=notification_text)

  return notification_text

