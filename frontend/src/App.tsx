import logo from "./assets/logo.svg";

export default function App() {
  return (
    <main className="min-h-screen bg-gradient-to-br from-blue-200 to-blue-600">
      <header className="bg-blue-900 text-blue-200 p-2 mb-4 w-full fixed top-0 left-0 z-10 flex justify-between items-center">
        <img src={logo} alt="CupoSmart Logo" className="h-12 w-auto mr-4" />
        <h1 className="text-center font-bold text-xl">CupoSmart</h1>
      </header>

      <footer className="text-center bg-blue-900 text-yellow-200 p-2 w-full">
        <p className="font-semibold">CupoSmart © 2023</p>
      </footer>
    </main>
  );
}
