import pandas as pd

# List of adapted SQL injection examples for Access
sql_injections = [
    "' OR '1'='1' --",
    "admin' --",
    "' OR 1=1; --",
    "'; DROP TABLE users; --",
    "'' OR '' = '' --",
    "' UNION SELECT * FROM keys --",
    "1234' AND '1'='1",
    "admin' OR 'x'='x' --",
    "' AND EXISTS(SELECT * FROM users WHERE username = 'admin') --",
    "' OR EXISTS(SELECT * FROM keys WHERE key_id = 1234) --",
    "username' OR 'a'='a' --",
    "' AND 'abc'='abc' --",
    "'; SELECT * FROM formblocklist --",
    "' OR LEN(password) > 0 --",
    "' UNION SELECT user_id, username FROM users WHERE '1'='1' --",
    "'' OR 1=1; --",
    "1234' OR 1=1 --",
    "'; UPDATE keys SET key_value = 'hacked' WHERE key_id = 1 --",
    "' OR 'x' > 'a' --",
    "' OR (SELECT COUNT(*) FROM users) > 0 --",
    "' UNION SELECT key_value, NULL FROM keys --",
    "' UNION SELECT NULL, username, password FROM users --",
    "1' UNION SELECT key_id FROM keys WHERE '1'='1' --",
    "' AND (SELECT COUNT(*) FROM formblocklist) > 0 --",
    "' UNION SELECT key_name, key_value FROM keys WHERE '1'='1' --",
    "' OR EXISTS (SELECT 1 FROM users WHERE user_id = 1) --",
    "1234' UNION SELECT key_value FROM keys --",
    "' AND IIF((SELECT COUNT(*) FROM keys) > 0, 1, 0) = 1 --",
    "' UNION SELECT NULL, NULL FROM formblocklist WHERE '1'='1' --",
    "' UNION SELECT password FROM users WHERE username = 'admin' --",
    "' AND 1=CDbl((SELECT key_value FROM keys WHERE key_id=1)) --",
    "' AND 1=(SELECT COUNT(*) FROM formblocklist WHERE blocklist_id=123) --",
    "' OR 1/0=0 --",
    "' AND (SELECT TOP 1 username FROM users) = 'admin' --",
    "' AND (SELECT COUNT(*) FROM keys) > 10 --",
    "1234' AND 1=CDbl((SELECT key_value FROM keys)) --",
    "' OR 'A' = 'B' --",
    "' AND ASC(MID((SELECT TOP 1 username FROM users), 1, 1)) > 64 --",
    "' AND 1 IN (SELECT user_id FROM users) --",
    "' AND (SELECT key_id FROM keys WHERE key_value LIKE '*test*') = 1 --",
    "' OR IIF(1=1, SLEEP(5), 0) --",
    "' AND (SELECT IIF(username = 'admin', SLEEP(3), 0)) --",
    "admin' OR IIF(1=1, NOW(), 'no-op') --",
    "' AND (SELECT COUNT(*) FROM users WHERE username='admin') > 0 --",
    "' AND IIF((SELECT COUNT(*) FROM keys)>10, SLEEP(3), 0) --",
    "1234' AND SLEEP(5) --",
    "' OR EXISTS(SELECT 1 FROM formblocklist WHERE blocklist_name = 'banned') --",
    "' AND IIF((SELECT COUNT(*) FROM users WHERE role='admin') > 0, 1, 0) --",
    "' OR NOT EXISTS(SELECT * FROM keys WHERE key_name = 'root') --",
    "' AND 1=CLng((SELECT key_value FROM keys WHERE key_id = 1234)) --"
]

# Create a Pandas DataFrame for easy handling
df = pd.DataFrame(sql_injections, columns=['SQL_Injection_Examples'])

def is_sql_injection(user_input):
    # Check if the user input is similar to any known SQL injection examples
    if user_input in df['SQL_Injection_Examples'].values:
        return True
    return False

# Test the function
user_input = input("Enter input to test for SQL injection: ")
if is_sql_injection(user_input):
    print("Denied, do not allow.")
else:
    print("Accepted, allow.")
