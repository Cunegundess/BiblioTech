import React from 'react'
import logo from '../../assets/logo-projeto.png';
import { Button } from '../Button';


import {
    BuscarInputContainer,
    Container,
    Input,
    Menu,
    MenuRight,
    Row,
    Wrapper,
} from './styles';

const Header = () => {
    return (
       <Wrapper>
            <Container>
                <Row>
                    <img src={logo} alt="logo bibliotech"/>
                    <BuscarInputContainer>
                        <Input placeholder='Buscar...'/>
                    </BuscarInputContainer>
                    <Menu>Live Code</Menu>
                    <Menu>Bibliotech</Menu>
                </Row>
                <Row>
                    <MenuRight href="#">home</MenuRight>
                    <Button title="Entrar"/>
                    <Button title="Cadastrar"/>
                </Row>
            </Container>
       </Wrapper>
    )
}

export { Header }