function extensions_apply(_a, _b, disable_all){
    var disable = []
    var update = []
    gradioApp().querySelectorAll('#extensions input[type="checkbox"]').forEach(function(x){
        if(x.name.startsWith("enable_") && ! x.checked) disable.push(x.name.substr(7))
        if(x.name.startsWith("update_") && x.checked) update.push(x.name.substr(7))
    })
    restart_reload()
    return [JSON.stringify(disable), JSON.stringify(update), disable_all]
}

function extensions_check(_, _){
    var disable = []
    gradioApp().querySelectorAll('#extensions input[type="checkbox"]').forEach(function(x){
        if(x.name.startsWith("enable_") && ! x.checked) disable.push(x.name.substr(7))
    })
    gradioApp().querySelectorAll('#extensions .extension_status').forEach(function(x){
        x.innerHTML = "Loading..."
    })
    var id = randomId()
    requestProgress(id, gradioApp().getElementById('extensions_installed_top'), null, null, null, false)
    return [id, JSON.stringify(disable)]
}

function install_extension_from_index(button, url){
    button.disabled = "disabled"
    button.value = "Installing..."
    textarea = gradioApp().querySelector('#extension_to_install textarea')
    textarea.value = url
    updateInput(textarea)
    gradioApp().querySelector('#install_extension_button').click()
}
