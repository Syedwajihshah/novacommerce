from novacommerce import main

def test_main_runs(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello from novacommerce!"