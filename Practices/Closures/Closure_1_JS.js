function html_tag(tag){
  function wrap_text(msg){
    console.log('<'+tag+'>'+ msg +'</'+tag+'>');
  }
  return wrap_text
}

print_h1 = html_tag('h1');
print_hello = html_tag('b')

print_h1('Test closure through JS')
print_hello('from print_hello')
