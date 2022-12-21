        newlink = link.get_attribute('data-url')
        driver.execute_script(f'''window.open({newlink},"_blank");''')