import { useState } from "react";
import styled from "styled-components";
import LoginForm from "../components/LoginForm";
import SignUpForm from "../components/SignUp";
function Login({ onLogin }) {
    const [showLogin, setShowLogin] = useState(true);
    return (
        <Wrapper>
            <Logo>BeatBazaar</Logo>
            {showLogin ? (
                <>
                    <LoginForm onLogin={onLogin} />
                    <Divider />
                    <p>
                        Don't have an account? &nbsp;
                        <button onClick={() => setShowLogin(false)}>
                            Sign Up
                        </button>
                    </p>
                </>
            ) : (
                <>
                    <SignUpForm onLogin={onLogin} />
                    <Divider />
                    <p>
                        Already have an account? &nbsp;
                        <button onClick={() => setShowLogin(true)}>
                            Log In
                        </button>
                    </p>
                </>
            )}
        </Wrapper>
    );
}
const Logo = styled.h1`
  font-family: "proxima nova";
  font-size: 4rem;
  color: #1134ff;
  margin: 8px 0 16px;
`;
const Wrapper = styled.section`
  max-width: 500px;
  margin: 40px auto;
  padding: 16px;
`;
const Divider = styled.hr`
  border: none;
  border-bottom: 1px solid #ccc;
  margin: 16px 0;
`;
export default Login;