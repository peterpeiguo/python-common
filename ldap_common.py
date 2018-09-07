import ldap

def search(ldap_url, cert_location, user, password, search_base, search_scope, search_condition):
    ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, ldap.OPT_X_TLS_NEVER)

    connection = ldap.initialize(ldap_url, bytes_mode=False)

    connection.set_option(ldap.OPT_REFERRALS, 0)
    connection.set_option(ldap.OPT_PROTOCOL_VERSION, 3)
    connection.set_option(ldap.OPT_X_TLS_CACERTFILE, cert_location)
    connection.set_option(ldap.OPT_X_TLS, ldap.OPT_X_TLS_DEMAND)
    connection.set_option(ldap.OPT_X_TLS_DEMAND, True)
    connection.set_option(ldap.OPT_DEBUG_LEVEL, 255)

    connection.simple_bind_s(user, password)
    return connection.search_s(search_base, search_scope, search_condition)