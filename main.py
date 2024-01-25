def assign_cookies(g, s):
    g.sort() #g is the greed factor or list of greed factors
    s.sort() # s is the size of the cookie or list of sizes of cookies

    content_children = 0
    current_cookie_size_index = 0


    for greed_factor in g:
        while current_cookie_size_index < len(s) and s[current_cookie_size_index] < greed_factor:
            current_cookie_size_index += 1

        if current_cookie_size_index < len(s):
            content_children += 1
            current_cookie_size_index += 1

    return content_children



