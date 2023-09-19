import { useNavigate } from 'react-router-dom';

import bannerImage from '../../assets/banner-book.png'
import { Button } from "../../components/Button";
import { Header } from "../../components/Header";


import { Container, TextContent, Title, TitleHightLight} from './styles';



const Home = () => {

    const navigate = useNavigate()

    const handleClickSignIn = () => {
        navigate ('/login')
    }

    return (<>
        <Header />
        <Container>
            <div>
                <Title>
                    <TitleHightLight>
                    Venha Conhecer á
                    <br />
                    </TitleHightLight>
                    Biblioteca do Futuro !
                </Title>
                <TextContent>
                Bem Vindo a maior
                    Biblioteca Online do Brasil!
                </TextContent>
                <Button title="Começar Agora" variant="secondary" onClick={handleClickSignIn}/>
            </div>
            <div>
                <img src={bannerImage} alt="Imagem principal" />
            </div>
        </Container>
    </> )
}

export { Home }