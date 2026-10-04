#!/usr/bin/env python3
"""Gera core.png via graph_models sem quebrar o `pdm run migrate`.

- Adiciona paths comuns do Graphviz no Windows ao PATH (cobre terminal
  com PATH desatualizado após instalar via winget/choco).
- Se o `dot` não existir, só avisa e sai com 0 para não falhar o migrate.
"""
import os
import shutil
import sys
from pathlib import Path

COMMON_DOT_DIRS = [
    r'C:\Program Files\Graphviz\bin',
    r'C:\Program Files (x86)\Graphviz\bin',
    str(Path.home() / 'AppData' / 'Local' / 'Programs' / 'Graphviz' / 'bin'),
    r'C:\ProgramData\chocolatey\bin',
]


def ensure_dot_in_path() -> bool:
    if shutil.which('dot'):
        return True
    for d in COMMON_DOT_DIRS:
        exe = Path(d) / 'dot.exe'
        if exe.is_file() and d not in os.environ.get('PATH', ''):
            os.environ['PATH'] = d + os.pathsep + os.environ.get('PATH', '')
            if shutil.which('dot'):
                print(f'[graph] Graphviz encontrado em: {d}')
                return True
    return shutil.which('dot') is not None


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    if str(root) not in sys.path:
        sys.path.insert(0, str(root))
    if not ensure_dot_in_path():
        print(
            '[graph] AVISO: executavel `dot` do Graphviz nao encontrado no PATH. '
            'Migrate OK, diagrama core.png nao atualizado. '
            'Instale com `winget install Graphviz.Graphviz` e reabra o terminal.'
        )
        return 0

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
    try:
        import django
        from django.core.management import call_command
    except ImportError as e:
        print(f'[graph] AVISO: Django indisponivel ({e}). Pulando diagrama.')
        return 0

    django.setup()
    try:
        call_command('graph_models', '-S', '-g', '-o', 'core.png', 'core')
    except Exception as e:  # pydotplus InvocationException cai aqui
        print(
            f'[graph] AVISO: nao foi possivel gerar core.png ({type(e).__name__}: {e}). '
            'Migrate OK, diagrama nao atualizado.'
        )
        return 0

    print('[graph] core.png atualizado.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
