


def serializererrorsmessage(error):
    print("Errors", error)
    if 'reset_token' in error:
        return "Reset Token is required to reset the password"
    elif 'old_password' in error:
        return "Old Password is required to change the password"
    elif 'new_password' in error:
        return "New Password is required to change the password"
    elif 'confirm_password' in error:
        return "Confirm Password is required to change the password"
    elif 'email' in error:
        return "Email is required for forgot password"
    elif 'non_field_errors' in error:
        return error['non_field_errors'][0]
