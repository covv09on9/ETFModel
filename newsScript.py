from selenium import webdriver
import time

def newsScriptAPI(date):
    url = f"https://news.naver.com/breakingnews/section/101/258?date={date}"
    