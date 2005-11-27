# TODO:
# - check version
# - check license
%define short_name equadiff
%define	texhash	[ ! -x %{_bindir}/texhash ] || %{_bindir}/texhash 1>&2 ;
Summary:	Formats for International conference on differential equations
Summary(pl):	Formaty dla miêdzynarodowej konferencji na temat równañ ró¿nicznowych
Name:		tetex-latex-%{short_name}
Version:	1.0
Release:	1
License:	LaTeX Project Public License
Group:		Applications/Publishing/TeX
Source0:	http://pc2.iam.fmph.uniba.sk/equadiff/proceedings/equadiff.cls
# Source0-md5:	50136ea9f16a63ae2051f180e17effce
Source1:	http://pc2.iam.fmph.uniba.sk/equadiff/proceedings/equadiff.sty
# Source1-md5:	7f1af73afeb59eff88edab978c37ef66
Source2:	http://pc2.iam.fmph.uniba.sk/equadiff/proceedings/equadiff10.clo
# Source2-md5:	ba0d7845ce5b471961c1409025bec349
Source3:	http://pc2.iam.fmph.uniba.sk/equadiff/proceedings/fig.ps
# Source3-md5:	5eb852762a6464d1cf6b26fc55a93113
Source4:	http://pc2.iam.fmph.uniba.sk/equadiff/proceedings/paper.pdf
# Source4-md5:	bfc8aadf48333e742d50ac210e90ae26
Source5:	http://pc2.iam.fmph.uniba.sk/equadiff/proceedings/paper.tex
# Source5-md5:	e0f4a0aff8d3ad6faafad14bfa5ac26a
URL:		http://pc2.iam.fmph.uniba.sk/equadiff/proceedings/
Requires(post,postun):	/usr/bin/texhash
Requires:	tetex-latex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LaTeX style format and instructions for preparation of manuscripts
Mini-symposia and Contributed talks of Equadiff 11 Conference.

%description -l pl
Format stylu LaTeXa i instrukcje do przygotowywania dokumentów
Mini-symposia i Contributed talks z konferencji Equadiff 11.

%prep
%setup -q -c -T
install %{SOURCE3} .
install %{SOURCE4} .
install %{SOURCE5} .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{short_name}

install %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{short_name}
install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{short_name}
install %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{short_name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%texhash

%postun
%texhash

%files
%defattr(644,root,root,755)
%doc *.tex *.pdf *.ps
%dir %{_datadir}/texmf/tex/latex/%{short_name}
%{_datadir}/texmf/tex/latex/%{short_name}/*.sty
%{_datadir}/texmf/tex/latex/%{short_name}/*.cls
%{_datadir}/texmf/tex/latex/%{short_name}/*.clo
