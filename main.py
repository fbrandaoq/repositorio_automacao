# importa bibliotecas
import pyautogui
import time
# tempo que cada comando demora para executar
pyautogui.PAUSE = 3
# instruções
'''pyautogui.press('win')
pyautogui.write('vscode')
pyautogui.press('enter')
# espera 10 segundos para abrir o vscode e continuar com os comandos
time.sleep(10)'''
# continua as instruções
pyautogui.hotkey('ctrl', 'shift', "'")
pyautogui.write('git init')
pyautogui.press('enter')
pyautogui.write('git add .')
pyautogui.press('enter')
pyautogui.write('git commit -m "Versão 1.0"')
# espera 5 segundos para dar tempo de fazer o commit
time.sleep(5)
# continua as instruções
pyautogui.press('enter')
pyautogui.write('git branch -m main')
pyautogui.press('enter')
pyautogui.write('git remote add origin https://github.com/fbrandaoq/repositorio_automacao.git')
pyautogui.press('enter')
pyautogui.write('git push -u origin main')
pyautogui.press('enter')