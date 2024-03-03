WAComponent subclass: HelloWorldComponent [
    renderContentOn: html [
        html text: 'Hello, World!'.
    ]
]


WAAdmin register: HelloWorldComponent asApplicationAt: 'hello'.


