# Branch: HEAD
# conditional build:
# _without_embed - don't build uClibc version
Summary:	Small bourne shell from Berkeley
Summary(de):	Kleine Bourne-Shell von Berkeley
Summary(fr):	Shell Bourne réduit de Berkeley
Summary(pl):	Ma³y shell bourne'a
Summary(tr):	Ufak bir bourne kabuðu
Name:		ash
Version:	0.4.0
Release:	5
License:	BSD
Group:		Applications/Shells
Source0:	%{name}-%{version}.tar.gz
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
PreReq:		fileutils
PreReq:		grep
BuildRequires:	glibc-static
BuildRequires:	flex
BuildRequires:	byacc
%if %{!?_without_embed:1}%{?_without_embed:0}
BuildRequires:	uClibc-devel
BuildRequires:	uClibc-static
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Conflicts:	mkinitrd <= 1.7

%define embed_path	/usr/lib/embed
%define embed_cc	%{_arch}-uclibc-cc
%define embed_cflags	%{rpmcflags} -Os

%define		_bindir		/bin

%description
ash is a bourne shell clone from Berkeley. It supports all of the
standard Bourne shell commands and has the advantage of supporting
them while remaining considerably smaller than bash.

%description -l de
ash ist ein Bourne-Shell-Clone aus Berkeley, der alle
Standard-Bourne-Shell- Befehle unterstützt und dennoch erheblich
weniger Platz beansprucht als bash.

%description -l fr
ash est un clone Berkeley du shell Bourne. Il gère toutes les
commandes standard du shell Bourne et a l'avantage de les gérer tout
en restant considérablement plus petit que bash.

%description -l pl
Ash jest klonem shella Bourne'a z Berkeley. Obs³uguje standardowe
komendy shella Bourne'a i jest mniejszy ni¿ bash.

%description -l tr
ash, Berkeley'in bir bourne kabuðu kopyasýdýr. Standart bourne kabuðu
komutlarýnýn tümünü destekler ve bash kabuðundan daha küçük olma
avantajýna sahiptir.

%package static
Summary:	Small bourne shell from Berkeley
Summary(de):	Kleine Bourne-Shell von Berkeley
Summary(fr):	Shell Bourne réduit de Berkeley
Summary(pl):	Ma³y shell bourne'a
Summary(tr):	Ufak bir bourne kabuðu
Group:		Applications/Shells
PreReq:		fileutils
PreReq:		grep
Conflicts:	mkinitrd <= 1.7

%description static
ash is a bourne shell clone from Berkeley. It supports all of the
standard Bourne shell commands and has the advantage of supporting
them while remaining considerably smaller than bash.

%description static -l de
ash ist ein Bourne-Shell-Clone aus Berkeley, der alle
Standard-Bourne-Shell- Befehle unterstützt und dennoch erheblich
weniger Platz beansprucht als bash.

%description static -l fr
ash est un clone Berkeley du shell Bourne. Il gère toutes les
commandes standard du shell Bourne et a l'avantage de les gérer tout
en restant considérablement plus petit que bash.

%description static -l pl
Ash jest klonem shella Bourne'a z Berkeley. Obs³uguje standardowe
komendy shella Bourne'a i jest mniejszy ni¿ bash.

%description static -l tr
ash, Berkeley'in bir bourne kabuðu kopyasýdýr. Standart bourne kabuðu
komutlarýnýn tümünü destekler ve bash kabuðundan daha küçük olma
avantajýna sahiptir.

%package embed
Summary:	Small bourne shell from Berkeley
Summary(de):	Kleine Bourne-Shell von Berkeley
Summary(fr):	Shell Bourne réduit de Berkeley
Summary(pl):	Ma³y shell bourne'a
Summary(tr):	Ufak bir bourne kabuðu
Group:		Applications/Shells

%description embed
ash is a bourne shell clone from Berkeley. It supports all of the
standard Bourne shell commands and has the advantage of supporting
them while remaining considerably smaller than bash. Version for
embedded systems.

%description embed -l pl
Ash jest klonem shella Bourne'a z Berkeley. Obs³uguje standardowe
komendy shella Bourne'a i jest mniejszy ni¿ bash. Wersja dla systemów
osadzonych.

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

%build
# BOOT
%if %{!?_without_embed:1}%{?_without_embed:0}
# some of this utilities does not compile with uClibc
# and it is not necessary
%{__make} mksignames mkbuiltins mknodes mksignames mksyntax mktokens
%{__make} \
	OPT_FLAGS="%{embed_cflags}" \
	CC=%{embed_cc}
mv -f sh ash-embed-shared
%{__make} \
	OPT_FLAGS="%{embed_cflags}" \
	LDFLAGS="-static" \
	CC=%{embed_cc}
mv -f sh ash-embed-static
%{__make} clean
%endif

# other
%{__make} OPT_FLAGS="%{rpmcflags}" LDFLAGS="-static %{rpmldflags}"
mv -f sh ash.static
%{__make} OPT_FLAGS="%{rpmcflags}" LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

# BOOT
%if %{!?_without_embed:1}%{?_without_embed:0}
install -d $RPM_BUILD_ROOT/%{embed_path}/{shared,static}
install ash-embed-static $RPM_BUILD_ROOT/%{embed_path}/static/ash
install ash-embed-shared $RPM_BUILD_ROOT/%{embed_path}/shared/ash
ln -sf ash $RPM_BUILD_ROOT/%{embed_path}/shared/sh
ln -sf ash $RPM_BUILD_ROOT/%{embed_path}/static/sh
%endif

# other
install -d $RPM_BUILD_ROOT/{%{_bindir},%{_mandir}/man1}
install sh $RPM_BUILD_ROOT%{_bindir}/ash
install ash.static $RPM_BUILD_ROOT%{_bindir}/ash.static
install sh.1 $RPM_BUILD_ROOT%{_mandir}/man1/ash.1
echo ".so ash.1" > $RPM_BUILD_ROOT%{_mandir}/man1/bsh.1
ln -sf ash $RPM_BUILD_ROOT/%{_bindir}/bsh

%post
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

%post static
if [ ! -f /etc/shells ]; then
	echo "%{_bindir}/ash.static" >> /etc/shells
else
	if ! grep -q '^%{_bindir}/ash.static$' /etc/shells ; then
		echo "%{_bindir}/ash.static" >> /etc/shells
	fi
fi

%preun
if [ "$1" = 0 ]; then
	grep -v '^%{_bindir}/ash$' /etc/shells | grep -v '^%{_bindir}/bsh$' > /etc/shells.new
	mv -f /etc/shells.new /etc/shells
fi

%preun static
if [ "$1" = 0 ]; then
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ash
%attr(755,root,root) %{_bindir}/bsh
%{_mandir}/man1/*

%files static
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ash.static

%if %{!?_without_embed:1}%{?_without_embed:0}
%files embed
%defattr(644,root,root,755)
%attr(755,root,root) %{embed_path}/*/*
%endif
