import {MdEmail, MdLock } from 'react-icons/md'

import { Button } from "../../components/Button";
import { Header } from "../../components/Header";
import { Input } from "../../components/Input";

import { Column, Container, CriarText, EsqueciText, Row, SubTitleLogin, Title, TitleLogin, Wrapper } from './styles';

const Login = () => {
    return (<>
        <Header />
        <Container>
            <Column>
                <Title>
                    Venha fazer parte da Maior Biblioteca tecnologica do mundo!
                    Com variedades de conteudo e entreterimento.
                </Title>
            </Column>
            <Column>
                <Wrapper>
                    <TitleLogin>Faça seu cadastro já</TitleLogin>
                    <SubTitleLogin>Faça seu Login e make the change.</SubTitleLogin>
                    <form>
                        <Input placeholder="E-mail" leftIcon={<MdEmail />}/>
                        <Input placeholder="Senha" type="password" leftIcon={<MdLock />}/>
                        <Button title="Entrar" variant="secondary" />
                    </form>
                    <Row>
                        <EsqueciText>Esqueci minha senha</EsqueciText>
                        <CriarText>Criar Conta</CriarText>
                    </Row>
                </Wrapper>
            </Column>
        </Container>
    </> )
}

export { Login }