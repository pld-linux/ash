#
# Conditional build
%bcond_without	static		# don't build static
%bcond_with	dietlibc	# link with dietlibc, implies without static
%bcond_with	uClibc		# link with uclibc
# Branch: HEAD

%if %{with dietlibc}
%undefine 	with_static
%endif

Summary:	Small bourne shell from Berkeley
Summary(de.UTF-8):	Kleine Bourne-Shell von Berkeley
Summary(es.UTF-8):	Pequeña shell bourne de Berkeley
Summary(fr.UTF-8):	Shell Bourne réduit de Berkeley
Summary(pl.UTF-8):	Mały shell bourne'a
Summary(pt_BR.UTF-8):	Pequena shell bourne de Berkeley
Summary(ru.UTF-8):	Облегченная версия Bourne shell (sh)
Summary(tr.UTF-8):	Ufak bir bourne kabuğu
Summary(uk.UTF-8):	Полегшена версія Bourne shell (sh)
Summary(zh_CN.UTF-8):	[系统]Berkeley的微型Bourne Shell
Summary(zh_TW.UTF-8):	[-A系$)B統]Berkeley的-A微$)B型Bourne Shell
Name:		ash
Version:	0.4.0
Release:	11
License:	BSD
Group:		Applications/Shells
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	1c59f5b62a081cb0cb3b053c01d79529
Patch0:		%{name}-builtin.patch
Patch1:		%{name}-echo.patch
Patch2:		%{name}-getcwd.patch
Patch3:		%{name}-getopt.patch
Patch4:		%{name}-glob.patch
Patch5:		%{name}-jobs.patch
Patch6:		%{name}-kill.patch
Patch7:		%{name}-makefile.patch
Patch8:		%{name}-manpage.patch
Patch9:		%{name}-hetio.patch
Patch10:	%{name}-memout.patch
Patch11:	%{name}-misc.patch
Patch12:	%{name}-redir.patch
Patch13:	%{name}-setmode.patch
Patch14:	%{name}-syntax.patch
Patch15:	%{name}-test.patch
Patch16:	%{name}-times.patch
Patch17:	%{name}-debian.patch
Patch18:	%{name}-ppid.patch
Patch19:	%{name}-freebsd.patch
Patch20:	%{name}-sighup.patch
Patch21:	%{name}-dietlibc.patch
Patch22:	%{name}-extern.patch
BuildRequires:	byacc
%{?with_dietlibc:BuildRequires:	dietlibc-devel}
BuildRequires:	flex
%if %{with static}
%{!?with_uClibc:BuildRequires: glibc-static}
%{?with_uClibc:BuildRequires: uClibc-static > 2:0.9.27-1}
%endif
%{?with_uClibc:BuildRequires: uClibc-devel > 2:0.9.27-1}
Requires(post,preun,verify):	grep
Requires(preun):	fileutils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Conflicts:	mkinitrd <= 1.7

%define		_bindir		/bin

%description
ash is a bourne shell clone from Berkeley. It supports all of the
standard Bourne shell commands and has the advantage of supporting
them while remaining considerably smaller than bash.

%description -l de.UTF-8
ash ist ein Bourne-Shell-Clone aus Berkeley, der alle
Standard-Bourne-Shell- Befehle unterstützt und dennoch erheblich
weniger Platz beansprucht als bash.

%description -l es.UTF-8
Ash es un clon del shell bourne de Berkeley. Soporta todos los
comandos padrón de la Bourne shell y tiene la ventaja de soportarlos
con un tamaño considerablemente menor del que bash.

%description -l fr.UTF-8
ash est un clone Berkeley du shell Bourne. Il gère toutes les
commandes standard du shell Bourne et a l'avantage de les gérer tout
en restant considérablement plus petit que bash.

%description -l pl.UTF-8
Ash jest klonem shella Bourne'a z Berkeley. Obsługuje standardowe
komendy shella Bourne'a i jest mniejszy niż bash.

%description -l pt_BR.UTF-8
ash é um clone do shell bourne de Berkeley. Ele suporta todos os
comandos-padrão da Bourne shell e tem a vantagem de suportá-los com um
tamanho consideravelmente menor do que bash.

%description -l ru.UTF-8
Шелл - это базовая системная программа, которая интерпретирует команды
пользователя, вводимые с клавиатуры или при помощи мыши. Ash - это
клон Bourne shell (sh) из Беркли. Ash поддерживает все стандартные
команды шелла sh, будучи значительно меньше чем sh. В ash отсутствуют
некоторые возможности Bourne shell (например, история команд), но он
требует значительно меньше памяти.

%description -l tr.UTF-8
ash, Berkeley'in bir bourne kabuğu kopyasıdır. Standart bourne kabuğu
komutlarının tümünü destekler ve bash kabuğundan daha küçük olma
avantajına sahiptir.

%description -l uk.UTF-8
Шел - це базова системна програма, котра інтерпретує команди
користувача, які вводяться з клавіатури або за допомогою миші. Ash -
це клон Bourne shell (sh) з Берклі. Ash підтримує усі стандартні
команди шела sh, будучи значно меншим ніж sh. В ash відсутні деякі
можливості Bourne shell (наприклад, історія команд), зате він вимагає
значно менше пам'яті.

%package static
Summary:	Small bourne shell from Berkeley
Summary(de.UTF-8):	Kleine Bourne-Shell von Berkeley
Summary(fr.UTF-8):	Shell Bourne réduit de Berkeley
Summary(pl.UTF-8):	Mały shell bourne'a
Summary(tr.UTF-8):	Ufak bir bourne kabuğu
Group:		Applications/Shells
Requires(post,preun,verify):	grep
Requires(preun):	fileutils
Conflicts:	mkinitrd <= 1.7

%description static
ash is a bourne shell clone from Berkeley. It supports all of the
standard Bourne shell commands and has the advantage of supporting
them while remaining considerably smaller than bash.

%description static -l de.UTF-8
ash ist ein Bourne-Shell-Clone aus Berkeley, der alle
Standard-Bourne-Shell- Befehle unterstützt und dennoch erheblich
weniger Platz beansprucht als bash.

%description static -l fr.UTF-8
ash est un clone Berkeley du shell Bourne. Il gère toutes les
commandes standard du shell Bourne et a l'avantage de les gérer tout
en restant considérablement plus petit que bash.

%description static -l pl.UTF-8
Ash jest klonem shella Bourne'a z Berkeley. Obsługuje standardowe
komendy shella Bourne'a i jest mniejszy niż bash.

%description static -l tr.UTF-8
ash, Berkeley'in bir bourne kabuğu kopyasıdır. Standart bourne kabuğu
komutlarının tümünü destekler ve bash kabuğundan daha küçük olma
avantajına sahiptir.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
# this is mainly for information, maybe add changelog to %doc?
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%{?_with_dietlibc:%patch21 -p1}
%patch22 -p1

%build
%if %{with static}
%{__make} \
%if %{with dietlibc}
	CC="diet %{__cc}" \
%else
%if %{with uClibc}
	CC="%{_target_cpu}-uclibc-gcc"\
%else
	CC="%{__cc}"
%endif
%endif
	OPT_FLAGS="%{rpmcflags} -Os" \
	LDFLAGS="-static %{rpmldflags}"

mv -f sh ash.static
%endif

%{__make} \
	CC="%{__cc}" \
	OPT_FLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install sh $RPM_BUILD_ROOT%{_bindir}/ash
%{?with_static:install ash.static $RPM_BUILD_ROOT%{_bindir}/ash.static}
install sh.1 $RPM_BUILD_ROOT%{_mandir}/man1/ash.1
echo ".so ash.1" > $RPM_BUILD_ROOT%{_mandir}/man1/bsh.1
ln -sf ash $RPM_BUILD_ROOT%{_bindir}/bsh

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
if [ ! -f /etc/shells ]; then
	echo "%{_bindir}/ash" > /etc/shells
	echo "%{_bindir}/bsh" >> /etc/shells
else
	if ! grep -q '^%{_bindir}/ash$' /etc/shells ; then
		echo "%{_bindir}/ash" >> /etc/shells
	fi
	if ! grep -q '^%{_bindir}/bsh$' /etc/shells ; then
		echo "%{_bindir}/bsh" >> /etc/shells
	fi
fi

%preun
if [ "$1" = 0 ]; then
	umask 022
	grep -v '^%{_bindir}/ash$' /etc/shells | grep -v '^%{_bindir}/bsh$' > /etc/shells.new
	mv -f /etc/shells.new /etc/shells
fi

%post static
umask 022
if [ ! -f /etc/shells ]; then
	echo "%{_bindir}/ash.static" >> /etc/shells
else
	if ! grep -q '^%{_bindir}/ash.static$' /etc/shells ; then
		echo "%{_bindir}/ash.static" >> /etc/shells
	fi
fi

%preun static
if [ "$1" = 0 ]; then
	umask 022
	grep -v '^%{_bindir}/ash\.static$' /etc/shells > /etc/shells.new
	mv -f /etc/shells.new /etc/shells
fi

%verifyscript
for n in ash bsh ; do
	echo -n "Looking for $n in /etc/shells... "
	if ! grep -q "^%{_bindir}/${n}\$" /etc/shells ; then
		echo "missing"
		echo "${n} missing from /etc/shells" >&2
	else
		echo "found"
	fi
done

%verifyscript static
echo -n "Looking for ash.static in /etc/shells... "
if ! grep -q '^%{_bindir}/ash\.static$' /etc/shells ; then
	echo "missing"
	echo "ash.static missing from /etc/shells" >&2
else
	echo "found"
fi

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ash
%attr(755,root,root) %{_bindir}/bsh
%{_mandir}/man1/*

%if %{with static}
%files static
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ash.static
%endif
