Summary:	Computer chess program
Summary(de):	Computerschachprogramm
Summary(es):	Juego de ajedrez de la GNU
Summary(fr):	Jeu d'Иchecs
Summary(pl):	Gra w szachy
Summary(pt_BR):	Jogo de xadrez da GNU
Summary(ru):	Шахматная программа GNU
Summary(tr):	Bilgisayar satranГ oyunu
Summary(uk):	Шахова програма GNU
Name:		gnuchess
Version:	4.0.pl80
Release:	10
License:	GPL
Group:		Applications/Games
#Source0:	ftp://ftp.gnu.org/pub/gnu/chess/%{name}-%{version}.tar.gz
Source0:	ftp://distfiles.pld-linux.org/by-md5/8/3/833110654ec086b4ace45e037612033e/%{name}-%{version}.tar.gz
# Source0-md5:	833110654ec086b4ace45e037612033e
Source1:	xchess.png
Source2:	%{name}.desktop
Patch0:		%{name}-fhs.patch
Patch1:		%{name}-ncurses.patch
Patch2:		%{name}-ac_fixes.patch
Icon:		xchess.xpm
BuildRequires:	autoconf
BuildRequires:	ncurses-devel >= 5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Provides:	chessprogram

%description
The gnuchess package contains the GNU chess program. By default,
GNUchess uses a curses text-based interface. Alternatively, GNUchess
can be used in conjunction with the xboard user interface and the X
Window System for a graphical chessboard.

%description -l de
Das berЭhmte GNU-Schachprogramm. Es ist textorientiert, kann aber mit
'xboard' verwendet werden, um X-orientiertes Schach zu spielen.

%description -l es
Este es el famoso programa de ajedrez de GNU. EstА basado en texto,
pero puede ser usado en conjunciСn con xboard para jugar ajedrez
basado en X.

%description -l fr
Le fameux programme de jeu d'Иchecs de GNU. Il est en mode texte mais
peut Йtre utilisИ avec xboard pour y jouer sous X.

%description -l pl
Oto sЁawny GNU program szachowy. Jest w trybie tekstowym, ale w
poЁ╠czeniu z xboard mo©e mieФ interfejs w X Window.

%description -l pt_BR
Este И o famoso programa de xadrez da GNU. и baseado em texto, mas
pode ser usado em conjunГЦo com xboard para jogar xadrez baseado em X.

%description -l ru
Пакет gnuchess содержит шахматную программу GNU. По умолчанию GNUchess
использует текстовый интерфейс на основе curses. Альтернативно она
может использоваться в сочетании с xboard, обеспечивающим графический
интерфейс под X Window System.

%description -l tr
Bu ЭnlЭ GNU satranГ programЩdЩr. Metin ekranda ГalЩЧЩr ama xboard
programЩ ile birlikte kullanЩlarak X altЩnda da oynanabilir.

%description -l uk
Пакет gnuchess м╕стить шахову програму GNU. За умовчанням GNUchess
використову╓ текстовий ╕нтерфейс на основ╕ curses. Альтернативно вона
може використовуватись у пар╕ з програмою xboard, яка забезпечу╓
граф╕чний ╕нтерфейс п╕д X Window System.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
cd src
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/games/gnuchess,%{_mandir}/man6} \
	$RPM_BUILD_ROOT{%{_applnkdir}/Games/Board,%{_pixmapsdir}}

cd src
%{__make} install prefix=$RPM_BUILD_ROOT%{_prefix} \
	exec_prefix=$RPM_BUILD_ROOT%{_prefix}

install %{SOURCE1} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_applnkdir}/Games/Board

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Games/Board/*
%{_pixmapsdir}/*
%{_datadir}/games/gnuchess
%{_mandir}/man6/*
