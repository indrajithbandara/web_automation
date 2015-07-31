# -*- coding: utf-8 -*-
from selenium import webdriver
import time
 
def capture(url, save_fn="capture.png"):
    browser = webdriver.Chrome()
    browser.set_window_size(1200, 900)
    browser.get(url)
    browser.execute_script(
        
        function () {
            var y = 0;
            var step = 100;
            window.scroll(0, 0);
 
            function f() {
                if (y &lt; document.body.scrollHeight) {
                    y += step;
                    window.scroll(0, y);
                    setTimeout(f, 50);
                } else {
                    window.scroll(0, 0);
                    document.title += "scroll-done";
                }
            }
 
            setTimeout(f, 1000);
        }
        );
 
    for i in xrange(30):
        if &quot;scroll-done&quot; in browser.title:
            break
        time.sleep(1)
 
    browser.save_screenshot(save_fn)
    browser.close()
 
if __name__ == &quot;__main__&quot;:
    capture(&quot;http://www.baidu.com&quot;)