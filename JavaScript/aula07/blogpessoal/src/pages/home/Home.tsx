

function Home() {
  return (
    <>
    <div style={{
        width: '100vw',
        display: 'flex',
        justifyContent: 'center'
    }}>
        <div>
            <div style={{
                width: '80vw',
                display: 'flex',
                flexDirection: 'column',
                alignItems: 'center'
            }}>
                <h2>Seja bem vindo!!!</h2>
                <p>Expresse aqui seus pensamentos e opiniões</p>
            </div>

            <div style={{
                width: '80vw',
                display: 'flex',
                flexDirection: 'column',
                alignItems: 'center'
            }}>
                <img src="https://kennydouglas.com.br/wp-content/uploads/2023/07/Fotografia-de-paisagem-guia-comp.webp" alt="Imagem da pag Home" width= '400px'/>
            </div>
        </div>
    </div>

    </>
  )
}

export default Home