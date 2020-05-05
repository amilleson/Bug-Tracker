$(document).ready(function(){
    $('#button1').click(function(){
        $('div.button').removeClass('btn2')
        $('div.button').addClass('btn')
        $('div.insert').html(
            `<div>
                <input type="text" name="email" placeholder="Email" class="input-field">
                <input type="password" name="password" placeholder="Enter Password" class="input-field">
                <button type="submit" class="btn-submit">Log In</button>
            </div>`)
        $('div.insert').parent().attr('action', '/login')
    }
    )
    $('#button2').click(function(){
        console.log('inside function')
        $('div.button').removeClass('btn')
        $('div.button').addClass('btn2')
        $('div.insert').html(
            `<div>
                <input type="text" name="first_name" class="input-field" placeholder="First Name">
                <input type="text" name="last_name" class="input-field" placeholder="Last Name">
                <input type="text" name="email" class="input-field" placeholder="Email">
                <input type="password" name="password" class="input-field" placeholder="Password">
                <input type="password" name="confirm_password" class="input-field" placeholder="Confirm Password">
                <button type="submit" class="btn-submit">Register</button>
            </div>`)
        $('div.insert').parent().attr('action', '/register')
        }
)})