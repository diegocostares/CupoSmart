import logo from "./assets/logo.svg";
import InputCourse from "./components/InputCourse";

export default function App() {
  return (
    <main className="min-h-screen flex flex-col bg-gradient-to-br from-blue-200 to-blue-600">
      <header className="bg-blue-900 text-blue-200 p-2 w-full fixed top-0 left-0 z-10 flex justify-between items-center mb-auto">
        <h1 className="text-center font-bold text-xl">CupoSmart</h1>
      </header>
      <section className="flex-1 flex justify-center items-center bg-gray-200 py-2">
        <div className="bg-white p-8 rounded-lg shadow-md w-96">
          <div className="mt-4 flex justify-center">
            <img src={logo} alt="Logo de CupoSmart" className="w-1/2" />
          </div>
          <h1 className="text-xl font-bold mb-4">
            Agrega las siglas de tus ramos
          </h1>
          {[...Array(5)].map((_, idx) => (
            <InputCourse key={idx} number={idx + 1} />
          ))}
          <button
            className="w-full bg-blue-500 hover:bg-blue-600 text-white p-2 rounded-md"
            aria-label="Calcular orden de inscripción"
          >
            Calcular orden inscripción
          </button>
        </div>
      </section>
      <footer className="text-center bg-blue-900 text-yellow-200 p-2 w-full mt-auto">
        <p className="font-semibold">CupoSmart © 2023</p>
      </footer>
    </main>
  );
}
